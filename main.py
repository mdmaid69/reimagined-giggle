  import sqlite3
  def close_database_connection(connection):
        connection.close()
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))