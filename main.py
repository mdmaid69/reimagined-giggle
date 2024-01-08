import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)