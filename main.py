import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)