  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)