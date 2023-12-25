import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)