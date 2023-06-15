from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import ProgrammingError
from pydantic import BaseModel


from backend import Sql_conn


# Variables to the model
class Query(BaseModel):
    select: str
    where : Optional[str]=None
    order_by : Optional[str]=None
    group_by : Optional[str]=None
    sort_by : Optional[str]=None

# Create our object of FastAPI
app = FastAPI()

# Based on the method post of analytics..
@app.post("/analytics")
async def query_data(query: Query):
    # ... we create  async function to get the result of a query 
    return Sql_conn().request_query(query.dict())
