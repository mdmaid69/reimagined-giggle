import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)