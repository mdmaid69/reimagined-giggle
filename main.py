import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)