import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)