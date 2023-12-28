import numpy as np
print(np.array([1, 2, 3]))
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))