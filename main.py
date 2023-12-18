def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()