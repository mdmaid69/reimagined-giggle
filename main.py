import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)