import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)