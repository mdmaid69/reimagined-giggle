import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)