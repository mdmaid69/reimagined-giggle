import math
def calculate_circle_area(radius):
        return math.pi * radius**2
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)