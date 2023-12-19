import math
def calculate_circle_area(radius):
        return math.pi * radius**2
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))