import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)