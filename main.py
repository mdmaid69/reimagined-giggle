def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")