  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)