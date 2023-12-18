import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)