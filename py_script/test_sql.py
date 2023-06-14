
from sqlalchemy import Column, Integer, String,text
from sqlalchemy import create_engine


DB_CONNSTR='postgresql://ps:ps_2023@localhost:5432/RAW'
Q = 'select num_age from newclients'
engine = create_engine(DB_CONNSTR, echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

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
with engine.connect() as conn:
    rs = conn.execute(text(Q))

    for row in rs:
        print(row)
