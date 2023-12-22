import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)