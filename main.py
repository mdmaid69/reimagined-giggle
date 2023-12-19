import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)