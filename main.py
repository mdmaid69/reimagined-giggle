import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)