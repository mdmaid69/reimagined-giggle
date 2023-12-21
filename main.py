import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
  def calculate_area_triangle(b, h):
        return 0.5 * b * h