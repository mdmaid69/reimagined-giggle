import re
def split_string(pattern, string):
        return re.split(pattern, string)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))