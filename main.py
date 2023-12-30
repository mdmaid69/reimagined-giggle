import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")