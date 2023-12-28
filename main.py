def calculate_area(radius):
        return 3.14 * radius * radius
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)