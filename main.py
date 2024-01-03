import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)