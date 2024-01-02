n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")