def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")