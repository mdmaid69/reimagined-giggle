import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)