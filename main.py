import math
def calculate_ceiling(x):
        return math.ceil(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))