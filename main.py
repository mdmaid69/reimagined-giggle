  import sqlite3
  def close_database_connection(connection):
        connection.close()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)