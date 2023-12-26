import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)