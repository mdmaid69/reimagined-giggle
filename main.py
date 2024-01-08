import math
def calculate_factorial(n):
        return math.factorial(n)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))