  import sqlite3
  def close_database_connection(connection):
        connection.close()
import collections
def create_stack():
        return collections.deque()