  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")