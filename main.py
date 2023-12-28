  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"