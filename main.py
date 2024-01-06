  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))