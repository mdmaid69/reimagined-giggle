  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")