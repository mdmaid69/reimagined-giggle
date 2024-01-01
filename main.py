import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)