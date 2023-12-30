  import sqlite3
  def close_database_connection(connection):
        connection.close()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)