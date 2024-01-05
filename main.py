import sys
def add_to_python_path(path):
        sys.path.append(path)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)