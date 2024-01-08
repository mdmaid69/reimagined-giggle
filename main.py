import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)