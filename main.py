import array
def get_array_slice(array, i, j):
        return array[i:j]
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)