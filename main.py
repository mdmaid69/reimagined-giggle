import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)