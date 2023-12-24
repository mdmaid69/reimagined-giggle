def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")