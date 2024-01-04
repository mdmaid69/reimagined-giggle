def calculate_perimeter_triangle(a, b, c):
        return a + b + c
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)