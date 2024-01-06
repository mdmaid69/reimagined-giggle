import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))