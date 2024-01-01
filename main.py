  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)