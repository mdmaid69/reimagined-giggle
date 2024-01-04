  import time
  def wait_for_seconds(seconds):
        time.sleep(seconds)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))