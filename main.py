import array
def set_array_item(array, i, item):
        array[i] = item
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))