  import math
  def calculate_square_root(n):
        return math.sqrt(n)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)