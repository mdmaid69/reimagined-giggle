import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")