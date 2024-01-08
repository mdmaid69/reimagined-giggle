import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")