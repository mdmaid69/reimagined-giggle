import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))