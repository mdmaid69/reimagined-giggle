def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)