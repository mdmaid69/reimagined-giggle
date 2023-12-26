import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)