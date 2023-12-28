import array
def get_array_slice(array, i, j):
        return array[i:j]
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)