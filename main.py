  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)