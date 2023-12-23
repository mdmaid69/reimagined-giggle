  def calculate_area_triangle(b, h):
        return 0.5 * b * h
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)