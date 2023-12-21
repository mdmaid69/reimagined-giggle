def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)