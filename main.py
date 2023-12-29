import array
def get_array_item_count(array, item):
        return array.count(item)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)