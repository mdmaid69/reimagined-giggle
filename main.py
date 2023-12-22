import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))