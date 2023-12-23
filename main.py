import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)