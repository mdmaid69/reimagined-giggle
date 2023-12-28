import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)