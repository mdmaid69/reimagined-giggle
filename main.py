import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def check_if_array_contains_item(array, item):
        return item in array