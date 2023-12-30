import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")