  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)