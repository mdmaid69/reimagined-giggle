  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)