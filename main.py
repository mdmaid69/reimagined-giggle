import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)