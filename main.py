import os
def get_file_size(filename):
        return os.path.getsize(filename)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)