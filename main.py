import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)