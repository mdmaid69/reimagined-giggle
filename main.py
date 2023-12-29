  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)