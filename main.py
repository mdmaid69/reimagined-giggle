import os
def list_files_in_directory(path):
        return os.listdir(path)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)