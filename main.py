import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")