def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)