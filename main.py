def add_numbers(a, b):
        return a + b
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)