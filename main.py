import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)