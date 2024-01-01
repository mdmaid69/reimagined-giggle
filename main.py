import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")