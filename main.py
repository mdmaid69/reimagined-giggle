import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)