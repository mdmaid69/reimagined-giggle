import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)