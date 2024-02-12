CREATE OR REPLACE EXTERNAL TABLE `terraform-demo-411511.ny_taxi.green_taxi_2022`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de-zoocamp-mage/green_taxi_data_2022/green_tripdata_2022-*.parquet']
)
;
-- question:1
CREATE OR REPLACE TABLE `terraform-demo-411511.ny_taxi.green_taxi_2022_nonpartitioned`
AS SELECT * FROM `terraform-demo-411511.ny_taxi.green_taxi_2022`;

-- question:2
SELECT COUNT(DISTINCT(PULocationID)) FROM `terraform-demo-411511.ny_taxi.green_taxi_2022`;
SELECT COUNT(DISTINCT(PULocationID)) FROM `terraform-demo-411511.ny_taxi.green_taxi_2022_nonpartitioned`;

-- question:3
SELECT COUNT(fare_amount) FROM `terraform-demo-411511.ny_taxi.green_taxi_2022`
WHERE fare_amount = 0;

-- question:4
CREATE OR REPLACE TABLE `terraform-demo-411511.ny_taxi.greentaxi_2022_partitioned`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PUlocationID AS (
  SELECT * FROM `terraform-demo-411511.ny_taxi.green_taxi_2022`
);

-- question:5
SELECT DISTINCT(PULocationID) FROM `terraform-demo-411511.ny_taxi.green_taxi_2022_nonpartitioned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';

SELECT DISTINCT(PULocationID) FROM `terraform-demo-411511.ny_taxi.greentaxi_2022_partitioned`
WHERE DATE(lpep_pickup_datetime) BETWEEN '2022-06-01' AND '2022-06-30';