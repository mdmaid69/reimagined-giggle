def calculate_area_circle(r):
        return 3.14 * r**2
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)