import array
def get_array_as_bool(array):
        return bool(array)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)