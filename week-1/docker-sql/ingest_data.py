import os
import sys
import ssl
import pandas as pd
import polars as pl
from dotenv import load_dotenv
from sqlalchemy import create_engine
from time import time 


# to use unverified ssl you can add this to your code:


ssl._create_default_https_context = ssl._create_unverified_context
load_dotenv()
#
DB_USER = os.getenv('DB_USER')
DB_PASSWARD = os.getenv('DB_PASSWARD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')




# use pandas 
def taxi_data_to_sql(file_url, insert_table_name):
    t_start = time()

    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    # if url.endswith('.csv.gz'):
    #     csv_name = 'output.csv.gz'
    # else:
    #     csv_name = 'output.csv'

    # os.system(f"wget {url} -O {csv_name}")
    df = pd.read_csv(file_url)
    print(df.head(5))

    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
    print(pd.io.sql.get_schema(df, name='yellow_taxi_data'))

    df.to_sql(insert_table_name, con=engine, if_exists='replace')
    t_end = time()

    print(f'inserted NY taxi data, took {(t_end - t_start)} second')

# use polars
def taxi_data_to_sql_pl(file_url, insert_table_name):

    if file_url.endswith('.csv'):
        df = pl.read_csv(file_url)
    elif file_url.endswith('.parquet'):
        df = pl.read_parquet(file_url)
    
    print(df.head(3))
    db_url = f"postgresql://{DB_USER}:{DB_PASSWARD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    t_start = time()
    df.write_database(table_name=insert_table_name, connection=db_url, if_table_exists='replace')
    t_end = time()

    print(f'inserted NY taxi data, took {(t_end - t_start)} second')
    
# taxi_data_to_sql("https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv", 'yellow_taxi_data')
taxi_data_to_sql_pl("https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2019-09.parquet", 'green_taxi_data')
taxi_data_to_sql_pl("https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv", 'taxi_zone')
