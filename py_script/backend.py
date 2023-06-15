from fastapi.templating import Jinja2Templates
from sqlalchemy import text

from models import engine, TABLE_NAME

# Import templates of Jinja2
templates = Jinja2Templates(directory="templates")

class Sql_conn:

    def _parse(self, query_dict: dict[str]):
        # Use dict to pass variables throught jinja template
        query_dict['table']= TABLE_NAME
        render = templates.TemplateResponse(
                "query_template.j2",{'request': None, 'data': query_dict}
            )
        return render.body.decode('ascii')

    def _query(self, q):
       # Use connection to make a query
        print(q)
        with engine.connect() as con:
            rs = con.execute(text(q))
        return rs
    def _resultdict(self,result):
        # Convert result to dict 
        resultdic = dict()
        for idx, row in enumerate(result):
            row_as_dict = row._mapping
            resultdic.update({idx:row_as_dict})
        return resultdic

    def request_query(self, query_dict: dict[str]):
        q = self._parse(query_dict)
        data = self._query(q)
        datadic = self._resultdict(data)
        return datadic
