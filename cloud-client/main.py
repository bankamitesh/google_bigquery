def run_quickstart():
    from google.cloud import bigquery

    client = bigquery.Client(project='yuktix-202507') #Project ID

    for dataset in client.list_datasets(): #Fetching all the Datasets that are already present
        print (dataset)

    dataset_id = 'Students' #New Dataset ID

    table_id = 'Information' #New Table ID

    dataset_ref = client.dataset(dataset_id) #Creating new Dataset
    dataset = bigquery.Dataset(dataset_ref)

    dataset = client.create_dataset(dataset)

    print('Dataset {} created.'.format(dataset.dataset_id))

    for dataset in client.list_datasets():
        print (dataset)

    #Schema for new Table
    schema = [
        bigquery.SchemaField('full_name', 'STRING', mode='REQUIRED'),
        bigquery.SchemaField('age', 'INTEGER', mode='REQUIRED'),
    ]

    table_ref = dataset_ref.table(table_id) #Creating new Table
    table = bigquery.Table(table_ref, schema=schema)
    table = client.create_table(table)  # API request

    assert table.table_id == table_id

    #Loading data into into the table from data.csv
    with open('data.csv', 'rb') as source_file: 
        job_config = bigquery.LoadJobConfig()
        job_config.source_format = 'text/csv'
        job = client.load_table_from_file(
            source_file, table_ref, job_config=job_config)

    job.result() 

    print('Loaded {} rows into {}:{}.'.format(job.output_rows, dataset_id, table_id))

    query = """ SELECT * FROM """ + dataset_id + """.""" + table_id + """ ORDER BY age"""#Query and View Data loaded into the table

    query_job = client.query(query)

    results = query_job.result()
    for row in results:
        print("{} : {}".format(row[0], row[1]))

if __name__ == '__main__':
    run_quickstart()