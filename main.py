import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))