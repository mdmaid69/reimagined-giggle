import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")