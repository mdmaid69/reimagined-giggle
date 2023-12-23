import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def insert_into_array(array, i, item):
        array.insert(i, item)