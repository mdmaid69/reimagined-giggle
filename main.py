import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")