import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)