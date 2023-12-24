  import sqlite3
  def close_database_connection(connection):
        connection.close()
import collections
def create_priority_queue():
        return collections.deque()