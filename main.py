def find_common_elements(list1, list2):
        return set(list1) & set(list2)
  import sqlite3
  def close_database_connection(connection):
        connection.close()