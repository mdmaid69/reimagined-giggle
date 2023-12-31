import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import os
def list_files_in_directory(path):
        return os.listdir(path)