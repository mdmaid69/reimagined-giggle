import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height