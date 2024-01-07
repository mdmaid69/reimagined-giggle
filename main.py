import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)