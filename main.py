import math
def calculate_absolute_value(x):
        return math.fabs(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))