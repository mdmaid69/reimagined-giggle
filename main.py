n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)