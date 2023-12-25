import array
def set_array_item(array, i, item):
        array[i] = item
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)