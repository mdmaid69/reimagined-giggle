import math
def calculate_hyperbolic_arc_sine(x):
        return math.asinh(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)