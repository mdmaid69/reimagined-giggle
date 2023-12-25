import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)