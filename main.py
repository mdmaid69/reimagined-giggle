import array
def get_array_buffer_info(array):
        return array.buffer_info()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)