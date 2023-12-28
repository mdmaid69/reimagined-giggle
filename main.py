import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)