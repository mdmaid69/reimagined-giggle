import array
def get_array_slice(array, i, j):
        return array[i:j]
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)