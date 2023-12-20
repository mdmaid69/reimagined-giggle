import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")