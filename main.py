import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}