import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)