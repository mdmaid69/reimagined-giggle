  import csv
  def write_to_csv_file(file_name, data):
        with open(file_name, "w", newline="") as file:
          writer = csv.writer(file)
          writer.writerows(data)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))