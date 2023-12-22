def calculate_area_rectangle(l, w):
        return l * w
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))