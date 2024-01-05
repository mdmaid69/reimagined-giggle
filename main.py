import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)