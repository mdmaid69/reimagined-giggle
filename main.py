import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)