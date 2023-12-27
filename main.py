  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"