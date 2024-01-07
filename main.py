import math
def calculate_absolute_value(x):
        return math.fabs(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)