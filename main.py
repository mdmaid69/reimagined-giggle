  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"