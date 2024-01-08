import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import csv
def save_csv(data, filename):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)