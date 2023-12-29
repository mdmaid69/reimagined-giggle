import math
def calculate_absolute_value(x):
        return math.fabs(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)