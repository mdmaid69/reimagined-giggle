import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)