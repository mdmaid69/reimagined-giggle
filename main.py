import array
def get_string_from_array(array):
        return array.tobytes()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)