import math
def calculate_cosine(x):
        return math.cos(x)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)