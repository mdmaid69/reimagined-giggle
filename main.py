import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)