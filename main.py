  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable