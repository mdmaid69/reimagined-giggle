import array
def get_array_as_repr(array):
        return repr(array)
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)