import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))