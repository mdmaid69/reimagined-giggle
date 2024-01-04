import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}