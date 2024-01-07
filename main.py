import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)