def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import sqlite3
  def close_database_connection(connection):
        connection.close()