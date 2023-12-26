import os
def get_file_size(filename):
        return os.path.getsize(filename)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)