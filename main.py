import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import sys
def add_to_python_path(path):
        sys.path.append(path)