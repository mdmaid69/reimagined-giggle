import array
def extend_array(array, iterable):
        array.extend(iterable)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)