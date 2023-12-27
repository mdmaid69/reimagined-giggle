import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))