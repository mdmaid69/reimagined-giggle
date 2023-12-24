  import sqlite3
  def close_database_connection(connection):
        connection.close()
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)