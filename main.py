import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)