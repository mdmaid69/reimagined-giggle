  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)