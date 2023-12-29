import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)