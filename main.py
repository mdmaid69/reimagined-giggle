n = 10
print("Powers of 2:", [2**x for x in range(n)])
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)