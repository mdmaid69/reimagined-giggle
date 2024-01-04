import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")