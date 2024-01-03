import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)