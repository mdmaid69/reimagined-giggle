n = 10
print("Square numbers:", [x**2 for x in range(n)])
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)