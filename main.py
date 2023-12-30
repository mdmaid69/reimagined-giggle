import math
def calculate_logarithm_base_e(x):
        return math.log(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)