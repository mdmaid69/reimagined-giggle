  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)