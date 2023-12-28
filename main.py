import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()