  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)