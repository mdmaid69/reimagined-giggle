import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)