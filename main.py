def calculate_force(mass, acceleration):
        return mass * acceleration
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)