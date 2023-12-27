import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")