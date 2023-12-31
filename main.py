import array
def get_array_as_float(array):
        return float(array[0])
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)