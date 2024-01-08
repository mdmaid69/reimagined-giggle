import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import sqlite3
  def close_database_connection(connection):
        connection.close()