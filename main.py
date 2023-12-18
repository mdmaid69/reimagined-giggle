import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)