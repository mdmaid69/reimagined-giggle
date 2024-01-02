import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)