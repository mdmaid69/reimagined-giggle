import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def append_to_array(array, item):
        array.append(item)