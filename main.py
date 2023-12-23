import array
def get_array_as_bool(array):
        return bool(array)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))