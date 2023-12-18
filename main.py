import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)