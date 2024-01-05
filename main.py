import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import sqlite3
  def execute_sql_query(connection, query):
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()