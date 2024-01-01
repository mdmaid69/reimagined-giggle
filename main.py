def calculate_area_triangle(b, h):
        return 0.5 * b * h
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)