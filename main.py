import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")