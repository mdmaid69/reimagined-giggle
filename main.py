import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)