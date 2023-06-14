
import os
from sqlalchemy import Column, String, Integer
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base

DB_CONNSTR = os.environ["DB_CONNSTR"]

engine = create_engine(DB_CONNSTR) if DB_CONNSTR else None
meta = MetaData(DB_CONNSTR)
Base = declarative_base(metadata=meta)


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
