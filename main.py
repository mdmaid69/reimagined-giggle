import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius