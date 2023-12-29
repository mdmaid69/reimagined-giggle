import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)