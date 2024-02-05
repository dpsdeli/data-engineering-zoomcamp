import io
import pandas as pd
import polars as pl
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    file_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet'
    # taxi_dtypes = {
    #     "VendorID":INT64,
    #     "tpep_pickup_datetime": TIMESTAMP,
    #     "tpep_dropoff_datetime":TIMESTAMP,
    #     "passenger_count":FLOAT64,
    #     "trip_distance":FLOAT64,
    #     "RatecodeID":FLOAT64,
    #     "store_and_fwd_flag":STRING,
    #     "PULocationID":INT64,
    #     "DOLocationID":INT64,
    #     "payment_type":INT64,
    #     "fare_amount":FLOAT64,
    #     "extra":FLOAT64,
    #     "mta_tax":FLOAT64,
    #     "tip_amount":FLOAT64,
    #     "tolls_amount":FLOAT64,
    #     "improvement_surcharge":FLOAT64,
    #     "total_amount":FLOAT64,
    #     "congestion_surcharge":FLOAT64,
    #     "airport_fee":FLOAT64
    # }

    if file_url.endswith('.csv'):
        df = pl.read_csv(file_url)
    elif file_url.endswith('.parquet'):
        df = pl.read_parquet(file_url)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
