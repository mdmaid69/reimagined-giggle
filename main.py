  import sqlite3
  def close_database_connection(connection):
        connection.close()
def count_characters(sentence):
        return len(sentence)