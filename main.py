import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)