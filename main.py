import math
def calculate_factorial(n):
        return math.factorial(n)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)