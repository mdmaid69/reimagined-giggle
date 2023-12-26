  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
def calculate_roi(gain, cost):
        return (gain - cost) / cost