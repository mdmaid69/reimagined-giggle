  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def remove_from_array(array, item):
        array.remove(item)