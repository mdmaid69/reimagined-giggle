def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")