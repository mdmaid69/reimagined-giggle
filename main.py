import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def get_array_slice(array, i, j):
        return array[i:j]