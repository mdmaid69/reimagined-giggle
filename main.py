import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
def count_elements(lst):
        return len(lst)