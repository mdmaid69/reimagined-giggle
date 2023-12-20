import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)