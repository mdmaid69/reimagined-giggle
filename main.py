import array
def get_string_from_array(array):
        return array.tobytes()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)