import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)