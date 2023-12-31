import json
print(json.dumps({"name": "John", "age": 30}))
import csv
def read_csv_file(filename):
        with open(filename, "r") as f:
        reader = csv.reader(f)
        return list(reader)