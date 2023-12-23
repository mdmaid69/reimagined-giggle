import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)