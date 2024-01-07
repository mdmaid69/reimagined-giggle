import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)