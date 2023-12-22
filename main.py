import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)