import array
def iterate_over_array(array):
        for item in array:
        print(item)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)