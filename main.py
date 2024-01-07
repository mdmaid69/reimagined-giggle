import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)