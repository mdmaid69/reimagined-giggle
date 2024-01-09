import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)