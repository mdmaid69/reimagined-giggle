import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)