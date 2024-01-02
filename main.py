import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def count_elements(lst):
        return len(lst)