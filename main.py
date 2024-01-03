import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3