import collections
def group_by(iterable, key_func):
        return collections.defaultdict(list, ((key, list(group)) for key, group in itertools.groupby(sorted(iterable, key=key_func), key_func)))
import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")