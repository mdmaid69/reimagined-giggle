import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)
import json
def read_from_json(json_string):
        return json.loads(json_string)