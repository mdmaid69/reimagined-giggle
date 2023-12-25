import array
def get_array_item(array, i):
        return array[i]
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)