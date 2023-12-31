def calculate_pressure(force, area):
        return force / area
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)