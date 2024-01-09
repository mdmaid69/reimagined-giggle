import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)