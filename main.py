import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")