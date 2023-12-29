import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)