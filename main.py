import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)