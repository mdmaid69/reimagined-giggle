  def is_odd(n):
        return n % 2 != 0
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))