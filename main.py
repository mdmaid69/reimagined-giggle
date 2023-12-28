text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)