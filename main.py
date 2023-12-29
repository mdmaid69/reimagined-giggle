import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)