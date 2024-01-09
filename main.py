import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)