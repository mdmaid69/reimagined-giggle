import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")