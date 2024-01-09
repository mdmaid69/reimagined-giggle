import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)