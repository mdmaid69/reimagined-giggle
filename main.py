  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))