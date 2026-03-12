import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv() # Load our .env

Base = declarative_base() # define our base that will link our classes, as they will inherit this declarative base for declarative mapping. declarative_base() returns a class so Base must be PascalCase

url_object = URL.create(
    "postgresql+psycopg2", # dialect + drivername
    username=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD"),
    host=os.getenv("PG_HOST"),
    database=os.getenv("PG_DATABASE")
)

engine = create_engine(url_object) # create engine using our url object

Session = sessionmaker(bind=engine) # created Session class configure to use engine
session = Session() # instantiate session