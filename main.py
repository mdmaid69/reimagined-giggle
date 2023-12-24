import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable