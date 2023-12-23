def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")