import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"