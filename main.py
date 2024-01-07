import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)