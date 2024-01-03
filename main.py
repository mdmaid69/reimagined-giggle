  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))