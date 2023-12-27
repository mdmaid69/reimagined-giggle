import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)