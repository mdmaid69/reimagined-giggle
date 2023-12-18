import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)