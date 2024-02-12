import io
import os
import requests
import pandas as pd
from google.cloud import storage
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

gcp_bucket = os.getenv('GCP_BUCKET')


def upload_to_gcs(bucket, destination_blob_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client(project=gcp_bucket)
    bucket = client.bucket(bucket)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_file)




def parquet_to_gcs(year):
    for i in range(12):
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        request_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_{year}-{month}.parquet" 
        
        # csv file_name
        file_name = f"green_tripdata_{year}-{month}.parquet"

        # read parquet file
        df = pd.read_parquet(request_url)
        df.to_parquet(f'./ny_taxi_data/{file_name}')
        
        # upload it to gcs 
        upload_to_gcs(gcp_bucket, f"green_taxi_data_2022/{file_name}", f'./ny_taxi_data/{file_name}')
        print(f"GCS: {file_name} upload")

parquet_to_gcs(2022)