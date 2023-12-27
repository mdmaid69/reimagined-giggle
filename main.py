import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def set_array_item(array, i, item):
        array[i] = item