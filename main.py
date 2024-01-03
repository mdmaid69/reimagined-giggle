  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)