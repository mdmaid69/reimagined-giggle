import math
def calculate_inverse_hyperbolic_cosine(x):
        return math.acosh(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)