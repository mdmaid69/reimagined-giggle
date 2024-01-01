import math
def calculate_arc_tangent(x):
        return math.atan(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))