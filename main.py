import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)