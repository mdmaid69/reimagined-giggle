import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))