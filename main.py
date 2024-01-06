import json
def read_from_json(json_string):
        return json.loads(json_string)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)