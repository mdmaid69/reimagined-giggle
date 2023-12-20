import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)