import math
def calculate_complementary_error_function(x):
        return math.erfc(x)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)