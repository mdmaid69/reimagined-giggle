  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import json
def convert_to_json(data):
        return json.dumps(data)