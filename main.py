import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)