sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))
  import sqlite3
  def close_database_connection(connection):
        connection.close()