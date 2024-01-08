import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)