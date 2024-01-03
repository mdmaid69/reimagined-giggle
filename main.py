import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)