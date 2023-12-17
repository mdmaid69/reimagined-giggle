  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import sqlite3
  def close_database_connection(connection):
        connection.close()