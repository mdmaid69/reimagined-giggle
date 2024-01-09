  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")