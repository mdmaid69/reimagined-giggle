  import sqlite3
  def close_database_connection(connection):
        connection.close()
import collections
def count_elements(iterable):
        return collections.Counter(iterable)