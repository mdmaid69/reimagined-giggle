import array
def get_list_from_array(array):
        return array.tolist()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)