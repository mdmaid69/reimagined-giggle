def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)