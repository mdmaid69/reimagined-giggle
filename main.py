import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)