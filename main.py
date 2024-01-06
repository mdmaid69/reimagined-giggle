import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))