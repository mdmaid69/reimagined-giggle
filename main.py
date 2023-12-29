import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import os
def change_working_directory(path):
        os.chdir(path)