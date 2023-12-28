import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)