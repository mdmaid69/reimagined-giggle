import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)