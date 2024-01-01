  import sqlite3
  def close_database_connection(connection):
        connection.close()
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))