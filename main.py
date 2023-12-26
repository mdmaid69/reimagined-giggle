  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")