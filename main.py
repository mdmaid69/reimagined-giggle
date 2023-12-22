import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)