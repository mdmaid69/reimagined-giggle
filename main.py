import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)