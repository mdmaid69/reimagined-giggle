import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import sqlite3
  def close_database_connection(connection):
        connection.close()