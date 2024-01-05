import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)