n = 10
print("Powers of 2:", [2**x for x in range(n)])
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)