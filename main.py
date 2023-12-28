import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)