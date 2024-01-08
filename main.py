  def calculate_perimeter_triangle(a, b, c):
        return a + b + c
  import csv
  def read_csv_file(file_name):
        with open(file_name, "r") as file:
          return list(csv.reader(file))