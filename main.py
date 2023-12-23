  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)