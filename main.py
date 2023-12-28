import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import re
def split_string(pattern, string):
        return re.split(pattern, string)