import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)