import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)