import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")