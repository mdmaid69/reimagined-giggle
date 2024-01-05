import platform
def get_python_version():
        return platform.python_version()
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))