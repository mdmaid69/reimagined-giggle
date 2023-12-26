import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)