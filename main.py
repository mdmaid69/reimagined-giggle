  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
from collections import Counter
print(Counter("hello world"))