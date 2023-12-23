import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import json
def convert_to_json(data):
        return json.dumps(data)