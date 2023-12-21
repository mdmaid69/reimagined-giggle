import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c