import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)