text = "Hello, world!"
print("Words:", len(text.split()))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)