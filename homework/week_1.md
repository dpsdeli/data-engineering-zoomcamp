# Module 1 Homework

## Questions

#### Question 1. Knowing docker tags
-- Which tag has the following text? - Automatically remove the container when it exits

Answer: 
    --rm  

#### Question 2. Understanding docker first run
-- Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash. Now check the python modules that are installed ( use pip list ).
What is version of the package wheel ?

Answer:
    0.42.0

##### Question 3. Count records
-- How many taxi trips were totally made on September 18th 2019? Tip: started and finished on 2019-09-18.

-- Remember that lpep_pickup_datetime and lpep_dropoff_datetime columns are in the format timestamp (date and hour+min+sec) and not in date.

Answer:
    15612

#### Question 4. Largest trip for each day
-- Which was the pick up day with the largest trip distance Use the pick up time for your calculations.

Answer: 
    2019-09-26

#### Question 5. Three biggest pick up Boroughs. The number of passengers
-- Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown. Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?

Answer:
    "Brooklyn" "Manhattan" "Queens"

#### Question 6. Largest tip
-- For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.
Note: it's not a typo, it's tip , not trip

Answer:
    JFK Airport

#### Question 7. Creating Resources
Answer:
    google_bigquery_dataset.demo_dataset: Creating... \
    google_storage_bucket.demo-bucket: Creating... \
    google_bigquery_dataset.demo_dataset: Creation complete after 2s [id=projects/terraform-demo-411511/datasets/Bigquery_demo_dataset] \
    google_storage_bucket.demo-bucket: Creation complete after 2s [id=terraform-demo-411511-bucket] \

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.