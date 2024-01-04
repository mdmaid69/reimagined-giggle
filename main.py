import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)