import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)