import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)