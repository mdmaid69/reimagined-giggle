import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)