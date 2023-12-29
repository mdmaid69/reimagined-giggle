import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)