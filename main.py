import array
def get_array_typecode(array):
        return array.typecode
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)