import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)