  import sqlite3
  def close_database_connection(connection):
        connection.close()
def count_words(sentence):
        return len(sentence.split())