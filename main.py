import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)