import array
def get_array_itemsize(array):
        return array.itemsize
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)