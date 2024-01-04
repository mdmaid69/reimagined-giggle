import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)