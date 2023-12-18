import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)