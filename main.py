import os
def remove_directory(path):
        os.rmdir(path)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)