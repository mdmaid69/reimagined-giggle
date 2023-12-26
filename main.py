def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")