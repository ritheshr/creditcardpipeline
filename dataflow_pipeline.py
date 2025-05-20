import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import logging

class CleanData(beam.DoFn):
    def process(self, element):
        import csv
        from datetime import datetime

        try:
            # Split row into fields
            row = list(csv.reader([element]))[0]
            
            # Ensure the row has the expected number of columns (e.g., 23 columns)
            if len(row) < 23:
                logging.warning(f"Skipping invalid row due to missing columns: {row}")
                return

            # Extract and sanitize the fields
            cust_id = row[0].strip() if row[0] else "UNKNOWN"
            balance = float(row[1]) if row[1] else 0.0
            credit_limit = float(row[2]) if row[2] else 0.0
            age = int(row[3]) if row[3] else 0
            gender = row[4].strip() if row[4] else "UNKNOWN"
            education = row[5].strip() if row[5] else "UNKNOWN"
            marriage = row[6].strip() if row[6] else "UNKNOWN"
            default = int(row[7]) if row[7] else 0

            yield {
                'cust_id': cust_id,
                'balance': balance,
                'credit_limit': credit_limit,
                'age': age,
                'gender': gender,
                'education': education,
                'marriage': marriage,
                'default': default
            }

        except Exception as e:
            logging.error(f"Error processing row {element}: {str(e)}")

# Define pipeline options
pipeline_options = PipelineOptions(
    runner='DataflowRunner',
    project='ecommerce-455605',  # Replace with your GCP project ID
    temp_location='gs://creditcard-sales-data-bucket/tmp',  # Replace with your GCS bucket
    region='us-central1'  # Replace if using a different region
)

# Define BigQuery Schema
BQ_SCHEMA = '''
    cust_id:STRING,
    balance:FLOAT,
    credit_limit:FLOAT,
    age:INTEGER,
    gender:STRING,
    education:STRING,
    marriage:STRING,
    default:INTEGER
'''

# Set the input and output locations
GCS_INPUT_PATH = 'gs://creditcard-sales-data-bucket/BankChurners.csv'  # Replace with your actual input path
BQ_TABLE = 'Creditcardusage.credit_card_customers'  # Replace with your actual BigQuery table

with beam.Pipeline(options=pipeline_options) as p:
    (p
     | 'Read CSV' >> beam.io.ReadFromText(GCS_INPUT_PATH, skip_header_lines=1)
     | 'Clean Data' >> beam.ParDo(CleanData())
     | 'Write to BigQuery' >> beam.io.WriteToBigQuery(
            BQ_TABLE,
            schema=BQ_SCHEMA,
            create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND  # Append to the table
        )
    )


