import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)