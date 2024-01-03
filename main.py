import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)