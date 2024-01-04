  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)