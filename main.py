import math
def calculate_arc_sine(x):
        return math.asin(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)