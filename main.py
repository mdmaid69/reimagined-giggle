  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array