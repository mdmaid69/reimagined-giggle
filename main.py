  import sqlite3
  def close_database_connection(connection):
        connection.close()
def find_difference(list1, list2):
        return set(list1) - set(list2)