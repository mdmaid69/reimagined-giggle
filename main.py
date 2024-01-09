import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)