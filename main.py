import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)