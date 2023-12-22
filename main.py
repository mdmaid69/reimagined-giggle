import array
def extend_array(array, iterable):
        array.extend(iterable)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))