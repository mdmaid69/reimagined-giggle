  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))