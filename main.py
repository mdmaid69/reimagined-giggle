  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def sort_numbers(numbers):
        return sorted(numbers)