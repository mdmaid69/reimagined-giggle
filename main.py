import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import json
def read_from_json(json_string):
        return json.loads(json_string)