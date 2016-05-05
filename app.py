from flask import Flask

from database import db_session
from flask_graphql import GraphQL
from schema import schema

app = Flask(__name__)
app.debug = True

default_query = '''
{
  allInvestedCompany (College:){
    edges {
      node {
        name,

      }
    }
  }
}'''.strip()

GraphQL(app, schema=schema, default_query=default_query)



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()