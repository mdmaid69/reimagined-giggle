  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")