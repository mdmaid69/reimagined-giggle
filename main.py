import math
def calculate_arc_cosine(x):
        return math.acos(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)