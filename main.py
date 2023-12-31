import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)