import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)