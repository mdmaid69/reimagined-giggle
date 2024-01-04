  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")