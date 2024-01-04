import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)