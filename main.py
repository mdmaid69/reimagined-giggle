  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))