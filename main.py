  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
import array
def convert_array_to_bytes(array):
        return array.tobytes()