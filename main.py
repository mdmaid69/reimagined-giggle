  def calculate_area_triangle(b, h):
        return 0.5 * b * h
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)