import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def extend_array(array, iterable):
        array.extend(iterable)