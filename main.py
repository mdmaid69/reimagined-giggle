import array
def remove_from_array(array, item):
        array.remove(item)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)