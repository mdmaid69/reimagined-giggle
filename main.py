  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)