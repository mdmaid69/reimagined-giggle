import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)