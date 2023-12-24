list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)