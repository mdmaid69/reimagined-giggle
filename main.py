sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import sqlite3
  def close_database_connection(connection):
        connection.close()