import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)