import array
def get_array_item(array, i):
        return array[i]
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)