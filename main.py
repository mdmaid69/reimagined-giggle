import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)