import requests
import pandas as pd

url = "https://api.covid19api.com/total/country/singapore/status/confirmed"
payload = {}

response = requests.request("GET", url, data=payload)
data = response.json()
df = pd.json_normalize(data)

df = df[['Date', 'Cases']]
df.to_csv('cases.csv', index=False)
