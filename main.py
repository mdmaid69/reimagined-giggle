sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)