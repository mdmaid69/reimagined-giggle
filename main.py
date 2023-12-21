import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)