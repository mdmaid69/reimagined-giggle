import array
def insert_into_array(array, i, item):
        array.insert(i, item)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))