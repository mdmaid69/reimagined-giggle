import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)