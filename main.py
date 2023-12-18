import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)