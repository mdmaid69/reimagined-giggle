import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)