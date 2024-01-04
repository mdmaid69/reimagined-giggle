import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)