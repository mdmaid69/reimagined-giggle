import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import array
def get_array_as_frozenset(array):
        return frozenset(array)