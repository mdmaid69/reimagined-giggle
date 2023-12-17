  import sqlite3
  def close_database_connection(connection):
        connection.close()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))