  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import pandas as pd
  def write_to_excel_file(file_name, data):
        df = pd.DataFrame(data)
        df.to_excel(file_name, index=False)