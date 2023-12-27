import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)