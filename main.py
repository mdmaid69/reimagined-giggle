  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")