
import os
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

# Use environment variable DB_CONNSTR
if os.environ["DB_CONNSTR"] is None:
    DB_CONNSTR='postgresql://ps:ps_2023@localhost:5432/RAW'
else:
    DB_CONNSTR = os.environ["DB_CONNSTR"]

# Create engine to connect our data base
engine = create_engine(DB_CONNSTR) if DB_CONNSTR else None
# Get all the metadata
meta = MetaData(DB_CONNSTR)
# declare metada has an object
Base = declarative_base(metadata=meta)

# Declare tables
TABLE_NAME='newclients'
class Newclients(Base):
    __tablename__ = TABLE_NAME
    num_age = Column(Integer, primary_key=True)
    des_employetype = Column(String, primary_key=True)
    is_graduate = Column(String, primary_key=True)
    imp_annualincome = Column(Integer, primary_key=True)
    num_familymembers = Column(Integer, primary_key=True)
    is_frequentflyer = Column(String, primary_key=True)
    is_evertravelledabroad= Column(String, primary_key=True)
