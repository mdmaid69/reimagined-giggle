  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))