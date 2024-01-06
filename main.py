import os
def get_environment_variable(var):
        return os.getenv(var)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)