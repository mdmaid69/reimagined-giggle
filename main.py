import math
def calculate_combinations(n, k):
        return math.comb(n, k)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))