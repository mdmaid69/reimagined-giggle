  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)