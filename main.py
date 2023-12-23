def calculate_force(mass, acceleration):
        return mass * acceleration
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)