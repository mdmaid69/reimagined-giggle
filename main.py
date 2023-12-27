import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)