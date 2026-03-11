import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv() # Load our .env

base = declarative_base() # define our base that will link our classes, as they will inherit this declarative base for declarative mapping

url_object = URL.create(
    "postgresql+psycopg2", # dialect + drivername
    username=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    database=os.getenv("POSTGRES_DATABASE")
)

engine = create_engine(url_object) # create engine using our url object

Session = sessionmaker(bind=engine) # created Session class configure to use engine
session = Session() # instantiate session