import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)