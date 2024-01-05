import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def get_array_slice(array, i, j):
        return array[i:j]