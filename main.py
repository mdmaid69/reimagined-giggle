import array
def convert_array_to_bytes(array):
        return array.tobytes()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)