import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)