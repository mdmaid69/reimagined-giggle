import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))