import math
def calculate_error_function(x):
        return math.erf(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)