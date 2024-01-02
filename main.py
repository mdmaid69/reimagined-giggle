import glob
def find_files(pattern):
        return glob.glob(pattern)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))