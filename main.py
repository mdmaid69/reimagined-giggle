import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))