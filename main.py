import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import csv
def load_csv(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)