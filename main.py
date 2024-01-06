import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import os
def get_file_size(filename):
        return os.path.getsize(filename)