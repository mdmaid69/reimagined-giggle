import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)