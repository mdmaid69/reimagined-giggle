import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)