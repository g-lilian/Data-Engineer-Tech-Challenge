# Data Engineer Tech Challenge

This test is split into 5 sections

1. **data pipelines**
2. **databases**
3. **system design**
4. **charts & APIs**
5. **machine learning**

## Submission Guidelines

Please create a Github repository containing your submission and send us an email containing a link to the repository.

Dos:

- Frequent commits
- Descriptive commit messages
- Clear documentation
- Comments in your code

Donts:

- Only one commit containing all the files
- Submitting a zip file
- Sparse or absent documentation
- Code which is hard to read

## Section 1: Data Pipelines

An e-commerce company requires that users sign up for a membership on the website in order to purchase a product from the platform. As a data engineer under this company, you are tasked with designing and implementing a pipeline to process the membership applications submitted by users on an hourly interval. 

Applications are batched into a varying number of datasets and dropped into a folder on an hourly basis. You are required to set up a pipeline to ingest, clean, perform validity checks, and create membership numbers for successful applications. An application is successful if:
- Application mobile number is 8 digits
- Applicant is over 18 years old as of 1 Jan 2022
- Applicant has a valid email (email ends with @emailprovider.com or @emailprovider.net)

You are required to format datasets in the following manner:
- Split name into first_name and last_name
- Format birthday field into YYYY/MM/DD
- Remove any rows which do not have a name field (treat this as unsuccessful applications)
- Create a new field named above_18 based on the applicant's birthday

You are required to consolidate these datasets and output the successful applications into a folder, which will be picked up by downstream engineers. Unsuccessful applications should be condolidated and dropped into a separate folder.

You can use common scheduling solutions such as cron or airflow to implement the scheduling component. Please provide a markdown file as documentation. 

Note: Please submit the processed dataset and scripts used