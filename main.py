import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)