def find_unique_words(sentence):
        return set(sentence.split())
  import sqlite3
  def close_database_connection(connection):
        connection.close()