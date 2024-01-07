import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import os
def get_environment_variable(var):
        return os.getenv(var)