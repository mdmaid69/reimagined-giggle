import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))