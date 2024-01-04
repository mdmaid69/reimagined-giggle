def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")