import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def set_array_item(array, i, item):
        array[i] = item