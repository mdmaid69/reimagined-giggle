import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height