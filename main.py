import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)