def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)