def calculate_area(radius):
        return 3.14 * radius * radius
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)