  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")