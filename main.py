import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)