import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)