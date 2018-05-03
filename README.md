# google_bigquery

Code Samples for Google BigQuery

Create A Simple Application with API 
(https://cloud.google.com/bigquery/create-simple-app-api)

Needed :- 
Google account
Credit/Debit Card

QuickStart (https://cloud.google.com/bigquery/quickstart-web-ui)

1. Select or create a GCP project.
GO TO THE MANAGE RESOURCES PAGE (https://console.cloud.google.com/cloud-resource-manager)

2. Make sure that billing is enabled for your project.
LEARN HOW TO ENABLE BILLING (https://cloud.google.com/billing/docs/how-to/modify-project)

3. BigQuery is automatically enabled in new projects. To activate BigQuery in a pre-existing project, go to Enable the BigQuery API.
ENABLE THE API (https://console.cloud.google.com/flows/enableapi?apiid=bigquery)


Before you begin make sure you have :- 

An understanding of BigQuery concepts and terminology.
Try the BigQuery Quickstart (https://cloud.google.com/bigquery/quickstart-web-ui) to get familiar with common BigQuery tasks.
A project with the BigQuery API enabled.
Applications that use BigQuery must be associated with a Google Cloud Platform Console (https://console.cloud.google.com/) project with the BigQuery API enabled.
A local development environment (Python).

Download the code for the sample command-line application and navigate into the app directory:

Clone the samples repository to your local machine.

git clone https://github.com/GoogleCloudPlatform/python-docs-samples

Alternatively, you can download the sample (https://github.com/GoogleCloudPlatform/python-docs-samples/archive/master.zip) as a zip file and extract it.

Change to the directory that contains the sample code:

cd python-docs-samples/bigquery/cloud-client

This sample uses the Google Cloud client libraries (https://cloud.google.com/bigquery/docs/reference/libraries) to make calls to the BigQuery API.

For more on installing and creating a BigQuery client, refer to BigQuery Client Libraries (https://cloud.google.com/bigquery/docs/reference/libraries).

Install the dependencies with pip (https://packaging.python.org/tutorials/installing-packages/).

pip install -r requirements.txt


Follow all Steps  in https://cloud.google.com/bigquery/docs/reference/libraries for Python

Code for Creating New Dataset, schema, tables, pushing data to table and to query data is in the python file main.py.
