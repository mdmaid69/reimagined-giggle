import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))