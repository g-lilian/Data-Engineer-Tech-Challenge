import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates


def plot_cases(start="2020-01-01", end="2022-11-21"):
    df = pd.read_csv('cases.csv')

    df = df[(df['Date'] > start) & (df['Date'] < end)]
    date = pd.to_datetime(df['Date'])
    num_cases = df['Cases']

    plt.plot_date(date, num_cases)
    plt.gcf().autofmt_xdate()
    date_format = mpl_dates.DateFormatter('%d-%m-%Y')
    plt.gca().xaxis.set_major_formatter(date_format)

    plt.tight_layout()
    plt.title('Cumulative num of confirmed Covid cases (Singapore)')
    plt.xlabel('Date')
    plt.ylabel('Num cases')
    plt.gca().get_yaxis().get_major_formatter().set_scientific(False)

    plt.savefig('graph.png', bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    plot_cases()
