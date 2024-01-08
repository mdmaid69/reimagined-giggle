import datetime
def get_current_datetime():
        return datetime.datetime.now()
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)