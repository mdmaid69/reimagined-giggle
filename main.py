import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)