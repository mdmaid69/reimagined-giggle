import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)