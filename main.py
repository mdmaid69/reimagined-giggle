import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)