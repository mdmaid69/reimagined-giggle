import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import sqlite3
  def close_database_connection(connection):
        connection.close()