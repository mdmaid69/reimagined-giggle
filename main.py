import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))