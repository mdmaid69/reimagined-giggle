  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)