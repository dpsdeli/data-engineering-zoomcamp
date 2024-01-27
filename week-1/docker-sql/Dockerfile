FROM python:3.10.9

RUN apt-get install wget
RUN pip install numpy pandas sqlalchemy psycopg2 polars pyarrow python-dotenv

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT [ "python", "ingest_data.py" ]