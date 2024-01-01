n = 10
print("Powers of 2:", [2**x for x in range(n)])
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)