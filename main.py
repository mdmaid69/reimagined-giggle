  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  import numpy as np
  def calculate_median(arr):
        return np.median(arr)