import array
def get_array_as_complex(array):
        return complex(array[0])
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)