import array
def append_to_array(array, item):
        array.append(item)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))