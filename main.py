import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)