import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)