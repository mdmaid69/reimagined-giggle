i = 0
while i < 5:
        print(i)
        i += 1
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)