import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")