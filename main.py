import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list