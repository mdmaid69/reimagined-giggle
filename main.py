import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def add_numbers(x, y):
        return x + y