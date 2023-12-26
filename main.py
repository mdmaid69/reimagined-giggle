  import sqlite3
  def close_database_connection(connection):
        connection.close()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))