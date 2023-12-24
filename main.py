import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)