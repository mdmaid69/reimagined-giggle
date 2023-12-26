  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)