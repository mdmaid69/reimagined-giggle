import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)