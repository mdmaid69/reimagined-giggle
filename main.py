import array
def get_array_itemsize(array):
        return array.itemsize
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)