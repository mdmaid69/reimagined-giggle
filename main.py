  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def pop_from_array(array, i=-1):
        return array.pop(i)