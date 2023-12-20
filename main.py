import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)