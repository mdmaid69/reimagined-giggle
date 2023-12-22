  def calculate_area_triangle(b, h):
        return 0.5 * b * h
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))