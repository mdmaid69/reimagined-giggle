import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height