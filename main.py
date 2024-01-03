import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))