import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)