import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)