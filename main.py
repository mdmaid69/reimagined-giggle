import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)