n = 10
print("Square numbers:", [x**2 for x in range(n)])
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)