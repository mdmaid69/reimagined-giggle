import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")