import array
def get_array_as_int(array):
        return int(array[0])
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))