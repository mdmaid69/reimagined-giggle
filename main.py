import math
def calculate_error_function(x):
        return math.erf(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))