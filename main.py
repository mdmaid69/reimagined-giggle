import array
def convert_array_to_unicode(array):
        return array.tounicode()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)