  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()