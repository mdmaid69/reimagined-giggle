import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))