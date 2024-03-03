# Module 5 Homework

In this homework we'll put what we learned about Spark in practice.

For this homework we will be using the FHV 2019-10 data found here.



## Questions

### Question 1: Install Spark and PySpark. What's the output? Spark version?
- 3.5.0


### Question 2: What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches?

"""
Read the October 2019 FHV into a Spark Dataframe with a schema as we did in the lessons.
Repartition the Dataframe to 6 partitions and save it to parquet.
"""

- 1MB
- 6MB [x]
- 25MB
- 87MB


### Question 3: How many taxi trips were there on the 15th of October? Consider only trips that started on the 15th of October.

- 108,164
- 12,856
- 452,470
- 62,610 [x]

### Question 4: What is the length of the longest trip in the dataset in hours?

- 631,152.50 Hours [x]
- 243.44 Hours
- 7.68 Hours
- 3.32 Hours


### Question 5: Spark’s User Interface which shows the application's dashboard runs on which local port?
- 80
- 443
- 4040 [x]
- 8080

### Question 6: Using the zone lookup data and the FHV October 2019 data, what is the name of the LEAST frequent pickup location Zone?
- East Chelsea
- Jamaica Bay[x]
- Union Sq
- Crown Heights North