import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)