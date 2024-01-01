  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
import itertools
print(list(itertools.permutations([1, 2, 3])))