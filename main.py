n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)