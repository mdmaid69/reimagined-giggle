def calculate_density(mass, volume):
        return mass / volume
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)