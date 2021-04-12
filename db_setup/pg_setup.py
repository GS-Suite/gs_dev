from typing import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

import os
from dotenv import load_dotenv
load_dotenv()

engine = create_engine("postgresql://poledahmmstoof:ff787d6bdafa96fd2132c35efff92a76a6bb4ad189948cdb7758fc1a4a341f72@ec2-54-73-58-75.eu-west-1.compute.amazonaws.com:5432/dbv10n31ojlgtb", echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()