def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")