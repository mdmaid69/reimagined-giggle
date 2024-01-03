import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import sqlite3
  def close_database_connection(connection):
        connection.close()