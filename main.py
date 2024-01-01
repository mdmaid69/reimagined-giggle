import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)