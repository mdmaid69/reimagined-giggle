import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)