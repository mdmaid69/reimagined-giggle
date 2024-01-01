import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)