import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)