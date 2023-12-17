import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))