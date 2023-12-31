  import math
  def calculate_square_root(n):
        return math.sqrt(n)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)