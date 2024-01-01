def find_min(lst):
        return min(lst)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)