  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))