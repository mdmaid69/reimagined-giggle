import array
def get_array_as_bytes(array):
        return bytes(array)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)