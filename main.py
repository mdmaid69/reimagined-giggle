  import sqlite3
  def close_database_connection(connection):
        connection.close()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)