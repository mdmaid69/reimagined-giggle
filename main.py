import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))