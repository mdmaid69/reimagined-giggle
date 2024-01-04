  import sqlite3
  def close_database_connection(connection):
        connection.close()
import json
def convert_to_json(data):
        return json.dumps(data)