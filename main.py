  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)