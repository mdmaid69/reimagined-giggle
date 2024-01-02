import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)