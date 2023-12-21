import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))