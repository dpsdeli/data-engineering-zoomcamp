import dlt
import duckdb
import sys

### Homework-1: Use a generator
'''
Remember the concept of generator? Let's practice using them to futher our understanding of how they work.
Let's define a generator and then run it as practice.
'''

def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)

for sqrt_value in generator:
    print(sqrt_value)

## Question-1: What is the sum of the outputs of the generator for limit = 5?

generator = square_root_generator(limit)
sum_outputs = sum(generator)
print("Sum of the square roots(limit=5):", sum_outputs)


## Question-2: What is the 13th number yielded?
limit = 13
generator = square_root_generator(limit)
result = [value for i, value in enumerate(generator) if i == limit - 1]
print(f'The 13th number yielded?: {result}')



### Homework-2: Append a generator to a table with existing data
"""
Below you have 2 generators. You will be tasked to load them to duckdb and answer some questions from the data

Load the first generator and calculate the sum of ages of all people. Make sure to only load it once.
Append the second generator to the same table as the first.
After correctly appending the data, calculate the sum of all ages of people.
"""
### Homework Question-3
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)

pipeline = dlt.pipeline(destination='duckdb', dataset_name='people_dataset')
load_info = pipeline.run(people_1(),
                        table_name="persons",
                        write_disposition="replace")

# view the "persons" table
duckdb_conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")
duckdb_conn.sql(f"SET search_path = '{pipeline.dataset_name}'")
print('---Loaded tables---')
print(duckdb_conn.sql("show tables"))

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}
for person in people_2():
    print(person)
load_info = pipeline.run(people_2(),
                        table_name="persons",
                        write_disposition="append")

# view the "persons" table
duckdb_conn.sql(f"SET search_path = '{pipeline.dataset_name}'")
persons = duckdb_conn.sql("SELECT * FROM persons").df()
print(persons)

sum_age = duckdb_conn.sql("""SELECT SUM("age") as all_ages FROM persons """).df()
print(f'sum of all ages of people: {sum_age}')

### Homework-3: Merge a generator 
"""
Re-use the generators from Exercise 2.
A table's primary key needs to be created from the start, so load your data to a new table with primary key ID.
Load your first generator first, and then load the second one with merge. Since they have overlapping IDs, some of the records from the first load should be replaced by the ones from the second load.
After loading, you should have a total of 8 records, and ID 3 should have age 33.
"""
## Question-4: Calculate the sum of ages of all the people loaded as described above.

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

for person in people_1():
    print(person)

pipeline = dlt.pipeline(destination='duckdb', dataset_name='people_dataset')
load_info = pipeline.run(people_1(),
                        table_name="members",
                        write_disposition="replace",
                        primary_key='id')

db_conn = duckdb.connect(f"{pipeline.pipeline_name}.duckdb")

# view the "members" table
db_conn.sql(f"SET search_path = '{pipeline.dataset_name}'")
members = db_conn.sql("SELECT * FROM members").df()
print(members)

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}

for person in people_2():
    print(person)

load_info = pipeline.run(people_2(),
                        table_name="members",
                        write_disposition="merge",
                        primary_key='id')


sum_age = db_conn.sql(""" SELECT SUM("age") as all_ages FROM members """).df()
print(sum_age)