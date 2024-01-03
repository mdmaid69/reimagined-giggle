  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)