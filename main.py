import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)