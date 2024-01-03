import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)