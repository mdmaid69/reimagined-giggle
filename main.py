import array
def get_array_as_frozenset(array):
        return frozenset(array)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)