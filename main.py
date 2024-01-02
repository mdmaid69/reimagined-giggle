import array
def get_array_buffer_info(array):
        return array.buffer_info()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)