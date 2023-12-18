  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))