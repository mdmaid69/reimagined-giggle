import math
def calculate_permutations(n, k):
        return math.perm(n, k)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)