import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)