import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")