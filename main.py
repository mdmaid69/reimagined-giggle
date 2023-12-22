import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)