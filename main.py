import re
print(re.match("h.*o", "hello world"))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)