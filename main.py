import array
def get_array_item_count(array, item):
        return array.count(item)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)