import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))