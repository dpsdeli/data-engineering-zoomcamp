# Week 1 Homework Answers

## Part A

### Question 1. Knowing docker tags
Run the command to get information on Docker

```docker --help```

Now run the command to get help on the "docker build" command
Which tag has the following text? - *Write the image ID to the file*

- `--imageid string`
- `--iidfile string`
- `--idimage string`
- `--idfile string`

### Answer

Typing `docker --help build` from the terminal command line print the output:
```
Usage:  docker build [OPTIONS] PATH | URL | -

Build an image from a Dockerfile

Options:
      --add-host list           Add a custom host-to-IP mapping (host:ip)
      --build-arg list          Set build-time variables
      --cache-from strings      Images to consider as cache sources
      --disable-content-trust   Skip image verification (default true)
  -f, --file string             Name of the Dockerfile (Default is 'PATH/Dockerfile')
      **--iidfile string          Write the image ID to the file**
      --isolation string        Container isolation technology
      --label list              Set metadata for an image
      --network string          Set the networking mode for the RUN instructions during build (default "default")
      --no-cache                Do not use cache when building the image
  -o, --output stringArray      Output destination (format: type=local,dest=path)
      --platform string         Set platform if server is multi-platform capable
      --progress string         Set type of progress output (auto, plain, tty). Use plain to show container output (default "auto")
      --pull                    Always attempt to pull a newer version of the image
...
```



### Question 2. Understanding docker first run

Run docker with the python:3.9 image in an interactive mode and the entrypoint of bash.
Now check the python modules that are installed ( use pip list).
How many python packages/modules are installed?

- 1
- 6
- 3
- 7


### Answer

By running:
```
docker run -it python:3.9.1 /bin/bash
```
running `pip list` within this container instance and show the output:
```
Package    Version
---------- -------
pip        21.0.1
setuptools 53.0.0
wheel      0.36.2
```

## Prepare Postgres

Run Postgres and load data as shown in the videos
We'll use the green taxi trips from January 2019:

```wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz```

You will also need the dataset with zones:

```wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv```

Download this data and put it into Postgres (with jupyter notebooks or with a pipeline)



### Question 3. Count records

How many taxi trips were totally made on January 15?

Tip: started and finished on 2019-01-15.

Remember that `lpep_pickup_datetime` and `lpep_dropoff_datetime` columns are in the format timestamp
(date and hour+min+sec) and not in date.

- 20689
- 20530
- 17630
- 21090

### Answer

The answer of SQL query:
```
SELECT COUNT(*)
FROM public.green_taxi_trips
WHERE (DATE(lpep_pickup_datetime)='2019-01-15'
AND DATE(lpep_dropoff_datetime)='2019-01-15');
```

There were **`20530`** taxi trips both started and finished on **`2019-01-15`**



### Question 4. Largest trip for each day

Which was the day with the largest trip distance?
Use the pick up time for your calculations.

- 2019-01-18
- 2019-01-28
- 2019-01-15
- 2019-01-10

### Answer

The answer of SQL query:
```
SELECT DATE(lpep_pickup_datetime)
FROM public.green_taxi_trips
ORDER BY trip_distance DESC
LIMIT 1;
```
The longest taxi drip distance occurred on **`2019-01-15`**.

### Question 5. The number of passengers

In 2019-01-01 how many trips had 2 and 3 passengers?

- 2: 1282 ; 3: 266
- 2: 1532 ; 3: 126
- 2: 1282 ; 3: 254
- 2: 1282 ; 3: 274


### Answer
The answer of SQL query:
```
WITH first_day_trips_table AS (
    SELECT passenger_count FROM public.green_taxi_trips
    WHERE DATE(lpep_pickup_datetime) = '2019-01-01'
    OR DATE(lpep_dropoff_datetime) = '2019-01-01'
),
    passengers_2_trips_table AS (
    SELECT COUNT(*) as count FROM first_day_trips_table
    WHERE passenger_count = 2
),
    passengers_3_trips_table AS (
    SELECT COUNT(*) as count FROM first_day_trips_table
    WHERE passenger_count = 3
)
SELECT passengers_2_trips_table.count FROM passengers_2_trips_table
       passengers_3_trips_table.count FROM passengers_3_trips_table;
```
- **`1282`** two-passenger trips: **`01-01-2019`**
- **`254`** three-passenger trips: **`01-01-2019`**



### Question 6. Largest tip

For the passengers picked up in the Astoria Zone which was the drop off zone that had the largest tip?
We want the name of the zone, not the id.

Note: it's not a typo, it's `tip` , not `trip`

- Central Park
- Jamaica
- South Ozone Park
- Long Island City/Queens Plaza

### Answer

The answer of SQL query:
```
WITH zone_table AS (
    SELECT "LocationID" AS id FROM public.taxi_zones
    WHERE "Zone" = 'Astoria'
),
largest_tip_id_table AS (
    SELECT "DOLocationID" AS id FROM public.green_taxi_trips
    WHERE "PULocationID" = (SELECT id FROM zone_table)
    ORDER BY tip_amount DESC
    LIMIT 1
),
largest_tip_name_table AS (
    SELECT "Zone" AS largest_tip_location FROM public.taxi_zones
    WHERE "LocationID" = (SELECT id FROM largest_tip_id_table)
)
SELECT largest_tip_location FROM largest_tip_name_table;
```
The **`Long Island City/Queens Plaza`** zone.