import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)