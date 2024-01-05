import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def find_min(lst):
        return min(lst)