import math
def calculate_inverse_hyperbolic_sine(x):
        return math.asinh(x)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)