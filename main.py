import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)