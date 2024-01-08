import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)