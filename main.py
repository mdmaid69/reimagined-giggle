  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)