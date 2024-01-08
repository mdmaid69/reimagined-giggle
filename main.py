import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")