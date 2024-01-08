import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)