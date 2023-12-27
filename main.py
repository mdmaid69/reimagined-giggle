import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)