from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import ProgrammingError
from pydantic import BaseModel
from backend import Sql_conn

class Query(BaseModel):
    select: str
    where : Optional[str]=None
    order_by : Optional[str]=None
    group_by : Optional[str]=None
    sort_by : Optional[str]=None


app = FastAPI()


@app.post("/analytics")
async def query_data(query: Query):
    return Sql_conn().request_query(query.dict())
