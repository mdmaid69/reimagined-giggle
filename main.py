import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)