import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")