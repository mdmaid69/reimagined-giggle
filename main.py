import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)