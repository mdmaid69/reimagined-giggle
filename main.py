import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)