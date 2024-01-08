  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")