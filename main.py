import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)