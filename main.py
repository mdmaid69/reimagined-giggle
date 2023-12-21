import array
def remove_from_array(array, item):
        array.remove(item)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)