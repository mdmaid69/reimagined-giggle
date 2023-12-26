import sklearn.datasets
print(sklearn.datasets.load_iris())
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()