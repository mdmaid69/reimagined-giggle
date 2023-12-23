  import sqlite3
  def close_database_connection(connection):
        connection.close()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)