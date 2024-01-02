import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()