def reverse_list(lst):
        return lst[::-1]
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)