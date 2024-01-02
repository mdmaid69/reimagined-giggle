  import sqlite3
  def close_database_connection(connection):
        connection.close()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)