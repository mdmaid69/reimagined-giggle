import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)