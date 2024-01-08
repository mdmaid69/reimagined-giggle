import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)