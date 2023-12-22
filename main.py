import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))