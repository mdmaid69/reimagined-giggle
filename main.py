import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)