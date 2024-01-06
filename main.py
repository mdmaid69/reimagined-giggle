def calculate_force(mass, acceleration):
        return mass * acceleration
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)