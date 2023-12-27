  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_distance(x1, y1, x2, y2):
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5