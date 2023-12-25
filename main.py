import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def pop_from_array(array, i=-1):
        return array.pop(i)