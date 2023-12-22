  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()