import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)