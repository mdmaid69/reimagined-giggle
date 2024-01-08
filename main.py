import math
def calculate_logarithm(base, x):
        return math.log(x, base)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))