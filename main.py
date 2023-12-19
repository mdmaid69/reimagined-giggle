import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
import array
def get_array_item_count(array, item):
        return array.count(item)