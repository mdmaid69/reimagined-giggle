import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)