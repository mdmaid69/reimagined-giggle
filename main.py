import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)