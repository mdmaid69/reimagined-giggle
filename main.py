import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)