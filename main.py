import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable