import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)