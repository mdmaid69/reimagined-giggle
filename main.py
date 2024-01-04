import array
def get_array_as_complex(array):
        return complex(array[0])
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)