import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)