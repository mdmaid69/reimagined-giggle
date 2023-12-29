import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))