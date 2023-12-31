import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
def find_union(list1, list2):
        return set(list1) | set(list2)