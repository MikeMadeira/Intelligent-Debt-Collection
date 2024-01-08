FROM python:3.9.1

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 faker

WORKDIR /synthetic-data-app
COPY generate_data.py generate_data.py 

ENTRYPOINT [ "python", "generate_data.py" ]