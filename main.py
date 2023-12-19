  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")