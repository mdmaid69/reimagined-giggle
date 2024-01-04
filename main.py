import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))