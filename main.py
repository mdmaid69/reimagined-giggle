import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")