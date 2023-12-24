  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def find_unique_words(sentence):
        return set(sentence.split())