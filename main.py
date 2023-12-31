import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)