import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)