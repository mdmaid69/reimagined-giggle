import array
def get_array_item_count(array, item):
        return array.count(item)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)