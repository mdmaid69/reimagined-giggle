import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)