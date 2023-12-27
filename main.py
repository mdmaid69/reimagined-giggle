import array
def get_array_as_set(array):
        return set(array)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)