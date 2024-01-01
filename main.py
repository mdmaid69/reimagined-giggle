import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)