  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_circumference_circle(r):
        return 2 * 3.14 * r