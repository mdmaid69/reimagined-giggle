import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)