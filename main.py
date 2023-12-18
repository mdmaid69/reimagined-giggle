def calculate_volume(length, width, height):
        return length * width * height
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)