import array
def check_if_array_contains_item(array, item):
        return item in array
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)