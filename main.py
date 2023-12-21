import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def sort_list(lst):
        return sorted(lst)