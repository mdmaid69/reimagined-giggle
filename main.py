  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import sqlite3
  def close_database_connection(connection):
        connection.close()