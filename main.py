import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)