def calculate_area_circle(r):
        return 3.14 * r**2
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)