import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)