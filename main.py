  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)