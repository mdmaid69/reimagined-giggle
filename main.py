n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)