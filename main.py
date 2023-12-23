import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))