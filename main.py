  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)