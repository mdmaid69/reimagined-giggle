  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))