import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))