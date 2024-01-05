import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)