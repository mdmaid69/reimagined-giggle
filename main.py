import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)