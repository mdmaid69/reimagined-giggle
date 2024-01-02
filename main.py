  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)