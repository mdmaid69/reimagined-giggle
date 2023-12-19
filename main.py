import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)