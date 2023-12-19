import json
def read_from_json(json_string):
        return json.loads(json_string)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)