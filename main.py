  def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)