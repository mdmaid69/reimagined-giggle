import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import sqlite3
  def close_database_connection(connection):
        connection.close()