import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))