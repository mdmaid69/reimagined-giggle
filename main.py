import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)