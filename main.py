import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)