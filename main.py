  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))