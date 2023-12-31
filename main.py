import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import collections
def create_ordered_dict():
        return collections.OrderedDict()