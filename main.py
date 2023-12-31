import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)