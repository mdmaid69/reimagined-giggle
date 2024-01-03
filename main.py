import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2