import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import sqlite3
  def close_database_connection(connection):
        connection.close()