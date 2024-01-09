import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")