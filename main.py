  import sqlite3
  def close_database_connection(connection):
        connection.close()
import json
def read_from_json(json_string):
        return json.loads(json_string)