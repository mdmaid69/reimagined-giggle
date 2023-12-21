import array
def check_if_array_contains_item(array, item):
        return item in array
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)